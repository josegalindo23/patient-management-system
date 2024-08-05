from src.infrastructure.controller import api_rest

if __name__ == "__main__":
    api_rest.app.register_error_handler(404,api_rest.page_not_found)
    api_rest.app.run(host="0.0.0.0", port=8080, debug=False)