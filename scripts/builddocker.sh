
REPO=taxtgg
IMAGE=zencastr
LONG_TAG=`git describe --abbrev=7 --tags --always --long --dirty`
SHORT_TAG=`git describe --abbrev=0`
SHORT_TAG="${SHORT_TAG:1}"

docker build -t ${IMAGE}:latest -t ${IMAGE}:${LONG_TAG} -t ${IMAGE}:${SHORT_TAG} .

docker tag ${IMAGE}:latest ${REPO}/${IMAGE}:latest
docker tag ${IMAGE}:${SHORT_TAG} ${REPO}/${IMAGE}:${SHORT_TAG}
docker tag ${IMAGE}:${LONG_TAG} ${REPO}/${IMAGE}:${LONG_TAG}

docker push ${REPO}/${IMAGE}:latest
docker push ${REPO}/${IMAGE}:${SHORT_TAG}
docker push ${REPO}/${IMAGE}:${LONG_TAG}
