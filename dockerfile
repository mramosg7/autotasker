FROM python:alpine
        
    EXPOSE 80
    
    WORKDIR /app
    
    COPY . /app
    
    
    RUN pip3 install -r requirements.txt
    
    RUN python manage.py collectstatic --noinput
    
    ENTRYPOINT ["python3"]
    CMD ["manage.py", "runserver", "0.0.0.0:80"]