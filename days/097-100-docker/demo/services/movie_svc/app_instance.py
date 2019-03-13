import responder

cors_params = {
    'allow_origins': '*',
    'allow_methods': '*',
}

api = responder.API(cors=True, cors_params=cors_params)
