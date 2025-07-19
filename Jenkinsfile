pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/prd1252/employee-time-tracker.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('employee-time-tracker')
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    docker.image('employee-time-tracker').run('-d -p 5000:5000')
                }
            }
        }
    }
}