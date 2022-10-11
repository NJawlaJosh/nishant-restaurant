def SendResponse(data, error=False):
    return {
        "error": error,
        "data": data
    }
