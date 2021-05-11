
```bash
# Install the requirements:
pip install -r requirements.txt

# Import data location of your MongoDB database:
mongorestore -d message-board ./message-board

# Start the server:
python main.py
```