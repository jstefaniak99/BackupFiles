pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Set up Python') {
            steps {
                sh 'sudo apt-get update && sudo apt-get install -y python3'
            }
        }

        stage('Run Script') {
            steps {
                sh 'python3 backupFiles.py'
            }
        }
    }
}
