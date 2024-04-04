# FastAPI project

To run the app execute 
```bash
uvicorn main:app --reload
```
This is also saved in `run_app.sh` for convenience. We can simply do 
```
bash run_app.sh
```

## Get items:
Run `request_get.sh` with 1 argument to get the ith item.
```
bash request_get.sh 1
```

## Post items:
Run `request_send.sh` with 1 argument to get the post/send an item to the API.
```
bash request_send abcd
```

