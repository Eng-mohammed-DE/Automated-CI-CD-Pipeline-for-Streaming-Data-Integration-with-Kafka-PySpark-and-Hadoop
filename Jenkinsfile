pipeline {
    agent any

    environment {
        VENV_DIR = '/home/eng-mohammed/master_node/venv'
        REQUIREMENTS_FILE = 'requirements.txt'
    }

    stages {

        stage('Debug VENV Path') {
            steps {
                script {
                    echo '🔍 Checking if virtual environment folder exists...'
                    sh "ls -la ${VENV_DIR} || echo '❌ Virtual environment folder not found.'"
                }
            }
        }

        stage('Create Virtual Environment') {
            steps {
                script {
                    echo '🔨 Checking if Virtual Environment needs to be created...'
                    if (!fileExists("${VENV_DIR}/bin/activate")) {
                        echo '❌ VENV not found. Creating...'
                        sh "python3 -m venv ${VENV_DIR}"
                    } else {
                        echo '✅ VENV already exists.'
                    }
                }
            }
        }

        stage('Verify Virtual Environment') {
            steps {
                script {
                    echo "📦 Verifying Virtual Environment setup..."
                    sh """
                        set -e
                        . ${VENV_DIR}/bin/activate
                        which python
                        python --version
                        which pip
                        pip --version
                    """
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    echo "📦 Installing Python dependencies..."
                    if (fileExists(REQUIREMENTS_FILE)) {
                        sh """
                            set -e
                            . ${VENV_DIR}/bin/activate
                            pip install -r ${REQUIREMENTS_FILE}
                        """
                    } else {
                        error "❌ ${REQUIREMENTS_FILE} not found!"
                    }
                }
            }
        }

        stage('Run Kafka Producer') {
            steps {
                script {
                    echo "🚀 Running Kafka Producer..."
                    sh """
                        set -e
                        . ${VENV_DIR}/bin/activate
                        python producer.py
                    """
                }
            }
        }

        stage('Run Spark Consumer') {
            steps {
                script {
                    echo "🚀 Running Spark Consumer..."
                    sh """
                        set -e
                        . ${VENV_DIR}/bin/activate
                        spark-submit --master local[*] consumer.py
                    """
                }
            }
        }

        stage('Clean Up') {
            steps {
                echo '🧹 Clean-up done.'
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully.'
        }
        failure {
            echo '❌ Pipeline failed.'
        }
    }
}
