pipeline {
  agent any

  environment {
    IMAGE_NAME = "your-dockerhub-username/ci-cd-sample"
  }

  stages {
    stage('Checkout') {
      steps {
        git branch: 'main', url: 'https://github.com/your-username/your-repo.git'
      }
    }

    stage('Build & Test') {
      steps {
        sh 'pip install -r requirements.txt'
        sh 'pytest -q'
      }
    }

    stage('Build Docker image') {
      steps {
        sh 'docker build -t $IMAGE_NAME:${BUILD_NUMBER} .'
      }
    }

    stage('Push Docker image') {
      steps {
        sh '''
          echo "docker login -u $DOCKERHUB_USER -p ****"
          echo "docker push $IMAGE_NAME:${BUILD_NUMBER}"
          echo "docker tag $IMAGE_NAME:${BUILD_NUMBER} $IMAGE_NAME:latest"
          echo "docker push $IMAGE_NAME:latest"
        '''
      }
    }

    stage('Deploy to staging') {
      steps {
        sh '''
          echo "docker pull $IMAGE_NAME:${BUILD_NUMBER}"
          echo "docker stop ci-cd-sample || true"
          echo "docker rm ci-cd-sample || true"
          echo "docker run -d --name ci-cd-sample -p 8000:5000 $IMAGE_NAME:${BUILD_NUMBER}"
        '''
      }
    }
  }
}
