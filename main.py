import uvicorn
from src.app import fast_api

if __name__ == '__main__':
    uvicorn.run(fast_api, host='0.0.0.0', port=8000)