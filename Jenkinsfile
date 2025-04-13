pipeline {
    agent any

    environment {
        // Point to the pre-created virtual environment's activate script
        VENV_PATH = '/home/eng-mohammed/master_node/venv/bin/activate'
        REQUIREMENTS_FILE = 'requirements.txt'
    }

    stages {
        stage('Verify Virtual Environment') {
            steps {
                script {
                    echo "📦 Checking Virtual Environment..."
                    sh '''
                        if [ -f ${VENV_PATH} ]; then
                            echo "✅ Virtual Environment exists."
                        else
                            echo "❌ Virtual Environment not found!"
                            exit 1
                        fi
                        . ${VENV_PATH}
                        which python
                        python --version
                        which pip
                        pip --version
                    '''
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    echo "🔧 Installing dependencies..."
                    // Ensure requirements.txt exists
                    if (fileExists(REQUIREMENTS_FILE)) {
                        sh '. ${VENV_PATH} && pip install -r ${REQUIREMENTS_FILE}'
                    } else {
                        error "❌ ${REQUIREMENTS_FILE} not found!"
                    }
                }
            }
        }

        stage('Run Kafka Producer') {
            steps {
                script {
                    echo "🎬 Running Kafka Producer..."
                    sh '. ${VENV_PATH} && python producer.py'
                }
            }
        }

        stage('Run Spark Consumer') {
            steps {
                script {
                    echo "🎬 Running Spark Consumer..."
                    sh '. ${VENV_PATH} && spark-submit --master local[*] consumer.py'
                }
            }
        }

        stage('Clean Up') {
            steps {
                echo '🧹 Cleaning up...'
                // Add any additional cleanup actions here if needed
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
