// Copyright 2016-2017, Pulumi Corporation.  All rights reserved.

package workspace

import (
	"encoding/json"
	"io/ioutil"
	"os"
	"path/filepath"
	"strings"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/pkg/pack"
	"github.com/pulumi/pulumi/pkg/resource/config"
	"github.com/pulumi/pulumi/pkg/tokens"
)

// W offers functionality for interacting with Pulumi workspaces.
type W interface {
	Settings() *Settings                 // returns a mutable pointer to the optional workspace settings info.
	Repository() *Repository             // returns the repository this project belongs to.
	StackPath(stack tokens.QName) string // returns the path to store stack information.
	GetPackage() (*pack.Package, error)  // returns a copy of the package associated with this workspace.
	Save() error                         // saves any modifications to the workspace.
}

type projectWorkspace struct {
	name     tokens.PackageName // the project this workspace is associated with.
	project  string             // the path to the Pulumi.[yaml|json] file for this project.
	settings *Settings          // settings for this workspace.
	repo     *Repository        // the repo this workspace is associated with.
}

// New creates a new workspace using the current working directory.
func New() (W, error) {
	cwd, err := os.Getwd()
	if err != nil {
		return nil, err
	}
	return NewFrom(cwd)
}

// NewFrom creates a new Pulumi workspace in the given directory. Requires a Pulumi.yaml file be present in the
// folder hierarchy between dir and the .pulumi folder.
func NewFrom(dir string) (W, error) {
	repo, err := GetRepository(dir)
	if err != nil {
		return nil, err
	}

	project, err := DetectPackageFrom(dir)
	if err != nil {
		return nil, err
	} else if project == "" {
		return nil, errors.New("no Pulumi project file found, are you missing a Pulumi.yaml file?")
	}

	pkg, err := pack.Load(project)
	if err != nil {
		return nil, err
	}

	w := projectWorkspace{
		name:    pkg.Name,
		project: project,
		repo:    repo}

	err = w.readSettings()
	if err != nil {
		return nil, err
	}

	if w.settings.Config == nil {
		w.settings.Config = make(map[tokens.QName]config.Map)
	}

	return &w, nil
}

func (pw *projectWorkspace) Settings() *Settings {
	return pw.settings
}

func (pw *projectWorkspace) Repository() *Repository {
	return pw.repo
}

func (pw *projectWorkspace) GetPackage() (*pack.Package, error) {
	return pack.Load(pw.project)
}

func (pw *projectWorkspace) Save() error {
	// let's remove all the empty entries from the config array
	for k, v := range pw.settings.Config {
		if len(v) == 0 {
			delete(pw.settings.Config, k)
		}
	}

	settingsFile := pw.settingsPath()

	// ensure the path exists
	err := os.MkdirAll(filepath.Dir(settingsFile), 0700)
	if err != nil {
		return err
	}

	b, err := json.MarshalIndent(pw.settings, "", "    ")
	if err != nil {
		return err
	}

	return ioutil.WriteFile(settingsFile, b, 0600)
}

func (pw *projectWorkspace) StackPath(stack tokens.QName) string {
	path := filepath.Join(pw.Repository().Root, StackDir, pw.name.String())
	if stack != "" {
		path = filepath.Join(path, qnamePath(stack)+".json")
	}
	return path
}

func (pw *projectWorkspace) readSettings() error {
	settingsPath := pw.settingsPath()

	b, err := ioutil.ReadFile(settingsPath)
	if err != nil && os.IsNotExist(err) {
		// not an error to not have an existing settings file.
		pw.settings = &Settings{}
		return nil
	} else if err != nil {
		return err
	}

	var settings Settings

	err = json.Unmarshal(b, &settings)
	if err != nil {
		return err
	}

	pw.settings = &settings
	return nil
}

func (pw *projectWorkspace) settingsPath() string {
	return filepath.Join(pw.Repository().Root, WorkspaceDir, pw.name.String(), WorkspaceFile)
}

// qnamePath just cleans a name and makes sure it's appropriate to use as a path.
func qnamePath(nm tokens.QName) string {
	return stringNamePath(string(nm))
}

// stringNamePart cleans a string component of a name and makes sure it's appropriate to use as a path.
func stringNamePath(nm string) string {
	return strings.Replace(nm, tokens.QNameDelimiter, string(os.PathSeparator), -1)
}
