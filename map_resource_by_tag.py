import json

def get_tags(openapi_data: dict) -> list:
    tags = []
    for tag in openapi_data.get('tags'):
        tags.append(tag.get('name'))
    return tags

def get_endpoints(openapi_data: dict) -> list:
    endpoints = []
    for path in openapi_data.get('paths'):
        for http_verb in openapi_data.get('paths').get(path):
            endpoint_tags = openapi_data.get('paths').get(path).get(http_verb).get('tags')
            endpoints.append({"path": path, "http_verb": http_verb, "tags": endpoint_tags})
    return endpoints

def reorder_endpoints_by_tag(tags: list, endpoints_details: list) -> dict:
    endpoints_by_tag = {}
    for tag in tags:
        endpoints_by_tag[tag] = []
        for endpoint in endpoints_details:
            if tag in endpoint.get('tags'):
                endpoints_by_tag[tag].append({"path": endpoint.get('path'), "http_verb": endpoint.get('http_verb')})                
    return endpoints_by_tag

def main():
    with open('swagger.json', 'r') as file:
        openapi_data = json.loads(file.read())
        tags = get_tags(openapi_data)
        endpoints_details = get_endpoints(openapi_data)
        enpoints_by_tag = reorder_endpoints_by_tag(tags, endpoints_details)
        print(json.dumps(enpoints_by_tag))

if __name__=='__main__':
    main()