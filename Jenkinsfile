pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git(
                    url: 'https://github.com/avi408/SiriAutomation.git',
                    branch: 'main',
                    credentialsId: 'github-avi408'
                )
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv .venv
                    source .venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    source .venv/bin/activate
                    behave --no-capture
                '''
            }
        }
    }

    post {
        always {
            echo 'Test execution completed.'
        }

        success {
            echo 'SiriAutomation pipeline PASSED.'
        }

        failure {
            echo 'SiriAutomation pipeline FAILED.'
        }
    }
}
