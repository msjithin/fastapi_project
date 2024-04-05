# FastAPI project

This is my first FastAPI app. This will be a place to try out ideas and experiment.
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
bash request_get.sh -id 5
```

## Post items:
Run `request_send.sh` with 1 argument to get the post/send an item to the API. By default, default 10 items will be added.
```
bash request_send.sh -item abcd
```

## Post items:
Run `request_items.sh` with 1 argument to get the list of items.
```
bash request_items.sh -limit 4
```

