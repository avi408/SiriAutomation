pipeline {

    agent any

    environment {
        PROJECT_DIR = "${WORKSPACE}"
        APPIUM_SERVER = "http://127.0.0.1:4723"
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out SiriAutomation from GitHub...'
                checkout scm
            }
        }

        stage('Environment') {
            steps {
                sh '''
                    echo "Python:"
                    python3 --version

                    echo "Node:"
                    node --version

                    echo "Appium:"
                    appium --version

                    echo "Xcode:"
                    xcodebuild -version
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/python -m pip install --upgrade pip
                    .venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Verify iOS Simulator') {
            steps {
                sh '''
                    echo "Checking iOS Simulator..."

                    xcrun simctl list devices | grep "iPhone 17 Pro"

                    xcrun simctl bootstatus \
                        AFE69C2B-4BB7-4AF5-B5E2-905719F47278 \
                        -b
                '''
            }
        }

        stage('Start Appium') {
            steps {
                sh '''
                    echo "Starting Appium..."

                    nohup appium \
                        --address 127.0.0.1 \
                        --port 4723 \
                        > appium.log 2>&1 &

                    sleep 5

                    curl --fail http://127.0.0.1:4723/status
                '''
            }
        }

        stage('Run BDD Tests') {
            steps {
                sh '''
                    mkdir -p reports/junit

                    .venv/bin/behave \
                        -f pretty \
                        -f junit \
                        -o reports/junit
                '''
            }
        }
    }

    post {

        always {

            echo 'Publishing test results...'

            junit allowEmptyResults: true,
                  testResults: 'reports/junit/*.xml'

            archiveArtifacts(
                artifacts: 'appium.log,reports/**/*,screenshots/**/*',
                allowEmptyArchive: true
            )
        }

        success {
            echo 'SiriAutomation pipeline completed successfully!'
        }

        failure {
            echo 'SiriAutomation pipeline failed.'
        }
    }
}

