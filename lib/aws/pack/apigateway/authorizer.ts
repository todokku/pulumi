// *** WARNING: this file was generated by the Lumi IDL Compiler (LUMIDL). ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

/* tslint:disable:ordered-imports variable-name */
import * as lumi from "@lumi/lumi";

import {RestAPI} from "./restAPI";
import {Role} from "../iam/role";

export let CognitoAuthorizer: AuthorizerType = "COGNITO_USER_POOLS";
export let TokenAuthorizer: AuthorizerType = "TOKEN";

export class Authorizer extends lumi.NamedResource implements AuthorizerArgs {
    public type: AuthorizerType;
    public authorizerCredentials?: Role;
    public authorizerResultTTLInSeconds?: number;
    public authorizerURI?: string;
    public identitySource?: string;
    public identityValidationExpression?: string;
    public providers?: lumi.Resource[];
    public restAPI?: RestAPI;

    public static get(id: lumi.ID): Authorizer {
        return <any>undefined; // functionality provided by the runtime
    }

    public static query(q: any): Authorizer[] {
        return <any>undefined; // functionality provided by the runtime
    }

    constructor(name: string, args: AuthorizerArgs) {
        super(name);
        if (args.type === undefined) {
            throw new Error("Missing required argument 'type'");
        }
        this.type = args.type;
        this.authorizerCredentials = args.authorizerCredentials;
        this.authorizerResultTTLInSeconds = args.authorizerResultTTLInSeconds;
        this.authorizerURI = args.authorizerURI;
        this.identitySource = args.identitySource;
        this.identityValidationExpression = args.identityValidationExpression;
        this.providers = args.providers;
        this.restAPI = args.restAPI;
    }
}

export interface AuthorizerArgs {
    type: AuthorizerType;
    authorizerCredentials?: Role;
    authorizerResultTTLInSeconds?: number;
    authorizerURI?: string;
    identitySource?: string;
    identityValidationExpression?: string;
    providers?: lumi.Resource[];
    restAPI?: RestAPI;
}

export type AuthorizerType =
    "COGNITO_USER_POOLS" |
    "TOKEN";

