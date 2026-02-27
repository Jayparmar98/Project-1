pipeline {
    agent any

    environment {
        IMAGE_NAME = "nlp-bot-qa"
        CONTAINER_NAME = "nlp-bot-container"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'qa', url: 'https://github.com/Jayparmar98/Project-1'
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
                docker run -d -p 5001:5001 --name $CONTAINER_NAME $IMAGE_NAME
                '''
            }
        }
    }
}