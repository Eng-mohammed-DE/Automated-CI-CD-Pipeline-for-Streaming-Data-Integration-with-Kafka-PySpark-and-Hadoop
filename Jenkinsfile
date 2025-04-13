pipeline {
    agent any

    environment {
        VENV_DIR = '/home/eng-mohammed/master_node/venv'
        REQUIREMENTS_FILE = 'requirements.txt'
    }

    stages {

        stage('Debug VENV Path') {
            steps {
                echo '🔍 Checking if virtual environment folder exists...'
                sh "ls -la ${VENV_DIR} || echo '❌ Virtual environment folder not found.'"
            }
        }

        stage('Create Virtual Environment') {
            steps {
                echo '🔨 Checking if Virtual Environment needs to be created...'
                sh """
                    if [ ! -f ${VENV_DIR}/bin/activate ]; then
                        echo '❌ VENV not found. Creating...'
                        python3 -m venv ${VENV_DIR}
                    else
                        echo '✅ VENV already exists.'
                    fi
                """
            }
        }

        stage('Verify Virtual Environment') {
            steps {
                echo "📦 Verifying Virtual Environment setup..."
                sh """
                    set +e
                    . ${VENV_DIR}/bin/activate
                    echo "Python path: $(which python)"
                    python --version
                    echo "Pip path: $(which pip)"
                    pip --version
                    set -e
                """
            }
        }

        stage('Install Dependencies') {
            steps {
                echo "📦 Installing Python dependencies..."
                sh """
                    set +e
                    if [ -f ${REQUIREMENTS_FILE} ]; then
                        . ${VENV_DIR}/bin/activate
                        pip install --upgrade pip
                        pip install -r ${REQUIREMENTS_FILE}
                        echo '✅ Dependencies installed successfully.'
                    else
                        echo "❌ ${REQUIREMENTS_FILE} not found!"
                        exit 1
                    fi
                    set -e
                """
            }
        }

        stage('Run Kafka Producer') {
            steps {
                echo "🚀 Running Kafka Producer..."
                sh """
                    set +e
                    . ${VENV_DIR}/bin/activate
                    echo "Running producer.py..."
                    python producer.py || { echo '❌ Kafka Producer failed'; exit 1; }
                    set -e
                """
            }
        }

        stage('Run Spark Consumer') {
            steps {
                echo "🚀 Running Spark Consumer..."
                sh """
                    set +e
                    . ${VENV_DIR}/bin/activate
                    echo "Running consumer.py with Spark..."
                    spark-submit --master local[*] consumer.py || { echo '❌ Spark Consumer failed'; exit 1; }
                    set -e
                """
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
