pipeline {
    agent any

    environment {
        VENV_DIR = '/home/eng-mohammed/master_node/venv'
        VENV_PATH = "${VENV_DIR}/bin/activate"
        REQUIREMENTS_FILE = 'requirements.txt'
    }

    stages {

        stage('Create Virtual Environment') {
            steps {
                script {
                    echo '🔨 Checking if Virtual Environment exists...'
                    if (!fileExists("${VENV_PATH}")) {
                        echo '❌ Virtual Environment not found. Creating it now...'
                        sh "python3 -m venv ${VENV_DIR}"
                    } else {
                        echo '✅ Virtual Environment already exists.'
                    }
                }
            }
        }

        stage('Verify Virtual Environment') {
            steps {
                script {
                    echo "📦 Verifying Virtual Environment..."
                    sh """
                        set -e
                        . ${VENV_PATH}
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
                    echo "🔧 Installing dependencies..."
                    if (fileExists(REQUIREMENTS_FILE)) {
                        sh """
                            set -e
                            . ${VENV_PATH}
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
                    echo "🎬 Running Kafka Producer..."
                    sh """
                        set -e
                        . ${VENV_PATH}
                        python producer.py
                    """
                }
            }
        }

        stage('Run Spark Consumer') {
            steps {
                script {
                    echo "🎬 Running Spark Consumer..."
                    sh """
                        set -e
                        . ${VENV_PATH}
                        spark-submit --master local[*] consumer.py
                    """
                }
            }
        }

        stage('Clean Up') {
            steps {
                echo '🧹 Cleaning up...'
                // Optional cleanup logic can go here
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
