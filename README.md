# FastAPI project

This is my first FastAPI app. This will be a place to try out ideas and experiment. This app is in a docker container. The docker image creation and running scripts are in `run_docker.sh`.
To run the app execute 
```bash
uvicorn main:app --reload
```
This is also saved in `run_app.sh` for convenience. We can simply do 
```
bash run_app.sh
```

To compose the docker, defining and running the container server
`docker-compose up --build `

## Create user:
Run
```
bash request_create_user.sh -u username@email.com -p password1234
```
## Create item:
We need to specify the user id, item title and description in the curl command. Run
```
bash request_create_item.sh 
```

## Get users:
Run `request_get_users.sh` 
```
bash request_get_users.sh 
```

## Get items:
Run `request_get_items.sh` with 1 argument to get the first ith items.
```
bash request_get_items.sh -limit 5
```

## Delete user and items
Follow scripts `request_delete_user.sh` and `request_delete_item.sh`. We need user id and item id respectively.
