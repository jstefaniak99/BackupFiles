pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('List branches') {
            steps {
                script {
                    sh 'git branch -r'
                }
            }
        }
    }
}
