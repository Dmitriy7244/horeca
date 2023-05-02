ENV_FILE_NAME=".env"

if [ ! -f $ENV_FILE_NAME ]; then
  echo "You must create file '$ENV_FILE_NAME'"
  return
fi

docker compose up --build --wait --remove-orphans
