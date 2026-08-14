pipeline {
    agent any

    environment {
    PATH = "/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
    PYTHON = "/Library/Frameworks/Python.framework/Versions/3.14/bin/python3"
    APPIUM = "/opt/homebrew/bin/appium"
    XRUN = "/usr/bin/xcrun"
    DEVICE = "iPhone 17 Pro"
    APPIUM_URL = "http://127.0.0.1:4723"
}

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out SiriAutomation from GitHub...'
                checkout scm
            }
        }

        stage('Environment Check') {
            steps {
                sh '''
                    echo "===== Environment ====="
                    $PYTHON --version
                    git --version
                    $APPIUM --version
                    $XRUN simctl list devices
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    echo "Creating Python virtual environment..."

                    rm -rf .jenkins-venv

                    $PYTHON -m venv .jenkins-venv

                    . .jenkins-venv/bin/activate

                    python --version
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Boot iPhone Simulator') {
            steps {
                sh '''
                    echo "Checking iPhone 17 Pro..."

                    $XRUN simctl boot "$DEVICE" 2>/dev/null || true

                    open -a Simulator

                    echo "Waiting for simulator..."
                    $XRUN simctl bootstatus "$DEVICE" -b

                    echo "Simulator is ready."
                '''
            }
        }

        stage('Start Appium') {
            steps {
                sh '''
                    echo "Starting Appium..."

                    nohup $APPIUM \
                        --address 127.0.0.1 \
                        --port 4723 \
                        > appium.log 2>&1 &

                    echo $! > appium.pid

                    echo "Waiting for Appium..."

                    for i in {1..30}; do
                        if curl -s "$APPIUM_URL/status" > /dev/null; then
                            echo "Appium is ready."
                            break
                        fi

                        sleep 2
                    done

                    curl -s "$APPIUM_URL/status"
                '''
            }
        }

        stage('Run Siri Tests') {
            steps {
                sh '''
                    . .jenkins-venv/bin/activate

                    mkdir -p reports

                    behave \
                        features/weather.feature \
                        --no-capture \
                        --name "Ask today's weather" \
                        | tee reports/behave-output.txt
                '''
            }
        }
    }

    post {

        always {
            echo 'Collecting test artifacts...'

            archiveArtifacts artifacts: 'reports/**, appium.log', 
                             allowEmptyArchive: true

            sh '''
                if [ -f appium.pid ]; then
                    kill $(cat appium.pid) || true
                fi
            '''
        }

        success {
            echo '====================================='
            echo 'SiriAutomation pipeline PASSED'
            echo '====================================='
        }

        failure {
            echo '====================================='
            echo 'SiriAutomation pipeline FAILED'
            echo '====================================='
        }
    }
}
