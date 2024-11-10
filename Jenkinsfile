pipeline {
    agent any

    stages {
        stage('Check Branch') {
            steps {
                script {
                    def branchName = env.BRANCH_NAME

                    // Sprawdzenie, czy commit nie idzie do /main
                    if (branchName == 'main') {
                        echo "Commit został zignorowany: nie można bezpośrednio commitować do /main!"
                        currentBuild.result = 'ABORTED'
                        return
                    } else {
                        echo "Commit został skierowany do poprawnego brancha"
                    }
                }
            }
        }

    }
}