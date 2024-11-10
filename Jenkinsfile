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
                sh '''
                python3 --version
                pip install --upgrade pip
                '''
            }
        }

        stage('Run File Copy Script') {
            steps {
                sh 'python3 backupFiles.py'
            }
        }
    }

    post {
        always {
            echo 'Pipeline zakończony.'
        }
        success {
            echo 'Kopiowanie plików zakończone pomyślnie!'
        }
        failure {
            echo 'Coś poszło nie tak. Sprawdź logi!'
        }
    }
}
