pipeline {
    agent any

    environment {
        VENV_PATH = '/home/eng-mohammed/master_node/venv/bin/activate'
    }

    stages {
        stage('Check Python & venv Availability') {
            steps {
                script {
                    sh '''
                        echo "🔍 Python & venv check..."
                        which python3
                        python3 --version
                        which pip
                        pip --version
                        python3 -m ensurepip || echo "❌ ensurepip not available"
                    '''
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Activate full venv path and install dependencies
                    sh '. ${VENV_PATH} && pip install -r requirements.txt'
                }
            }
        }

        stage('Run Kafka Producer') {
            steps {
                script {
                    sh '. ${VENV_PATH} && python producer.py'
                }
            }
        }

        stage('Run Spark Consumer') {
            steps {
                script {
                    sh '. ${VENV_PATH} && spark-submit --master local[*] consumer.py'
                }
            }
        }

        stage('Clean Up') {
            steps {
                script {
                    echo '🧹 Cleaning up...'
                }
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline ran successfully.'
        }
        failure {
            echo '❌ Pipeline failed.'
        }
    }
}
