-include /myenv

# config virtual environment
config:; source myenv/bin/activate

# run app using uvicorn
app-server:; uvicorn app:main --reload

# database session