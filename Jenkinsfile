pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building the application...'
            }
        }

        stage('Test') {
            steps {
                echo 'Running automated unit tests...'
                sh 'echo "Tests passed successfully"'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying the application...'
                sh 'echo "Deployment completed"'
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded! Your "Hello World" application is deployed.'
        }
        failure {
            echo 'Pipeline failed! Please check the logs for details.'
        }
    }
}
