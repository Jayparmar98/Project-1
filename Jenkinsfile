pipeline {
    agent any

    environment {
        IMAGE_NAME = "nlp-sentiment-dashboard"
        CONTAINER_NAME = "nlp-dashboard-container"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'dev', url: 'https://github.com/YOUR_USERNAME/nlp-sentiment-dashboard.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                docker stop $CONTAINER_NAME || true
                docker rm $CONTAINER_NAME || true
                docker run -d -p 80:5000 --name $CONTAINER_NAME $IMAGE_NAME
                '''
            }
        }
    }
}