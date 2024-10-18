from string import Template


def get_dockerfile_template(language: str, port: int, version: str) -> str:
    """
    Returns the Dockerfile template for the specified language and version.

    Args:
        language (str): The programming language for the Dockerfile.
        version (str): The version of the programming language.
        port (float): The port on which the container will run.

    Returns:
        str: The Dockerfile template.
    """

    version = version + '-alpine'

    if language == 'django' and version == 'lts-alpine':
        version = 'alpine'

    templates = {
        'django': f'''FROM python:{version}
        
    EXPOSE {port}
    
    WORKDIR /app
    
    COPY . /app
    
    RUN pip3 install -r requirements.txt
    
    ENTRYPOINT ["python3"]
    CMD ["manage.py", "runserver", "0.0.0.0:{port}"]''',
            'vite': f'''FROM node:{version} AS build
    
    WORKDIR /app
    
    COPY package.json /app
    COPY package-lock.json /app
    RUN npm install
    
    COPY . /app
    RUN npm run build
    
    FROM nginx:alpine
    COPY --from=build /app/dist /usr/share/nginx/html
    EXPOSE {port}
    CMD ["nginx", "-g", "daemon off;"]
    ''',
        'react': f'''FROM node:{version} AS build

    WORKDIR /app

    COPY package.json /app
    COPY package-lock.json /app
    RUN npm install

    COPY . /app
    RUN npm run build

    FROM nginx:alpine
    COPY --from=build /app/build /usr/share/nginx/html
    EXPOSE {port}
    CMD ["nginx", "-g", "daemon off;"]
    '''
    }
    return templates.get(language.lower(), "Unsupported language")
