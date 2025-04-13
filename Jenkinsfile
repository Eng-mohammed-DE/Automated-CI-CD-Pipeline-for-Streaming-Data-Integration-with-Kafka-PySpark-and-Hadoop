pipeline {
    agent any

    environment {
        PYTHON_ENV = '/home/eng-mohammed/master_node/venv/bin/activate'
    }

    stages {
        stage('Check if venv Exists') {
            steps {
                script {
                    if (fileExists('venv')) {
                        echo '⚠️ venv directory already exists. Skipping the rest of the pipeline...'
                        // Mark as success but stop further stages
                        currentBuild.result = 'SUCCESS'
                        error('Pipeline exited early because venv already exists.')
                    } else {
                        echo '✅ No existing venv. Proceeding with pipeline...'
                    }
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    sh '''
                        echo "📦 Creating virtual environment and installing dependencies..."
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Kafka Producer') {
            steps {
                script {
                    sh '''
                        echo "🚀 Running Kafka Producer..."
                        . venv/bin/activate
                        python producer.py
                    '''
                }
            }
        }

        stage('Run Spark Consumer') {
            steps {
                script {
                    sh '''
                        echo "🧠 Running Spark Consumer..."
                        . venv/bin/activate
                        spark-submit --master local[*] consumer.py
                    '''
                }
            }
        }

        stage('Clean Up') {
            steps {
                script {
                    echo '🧹 Cleaning up resources...'
                }
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline ran successfully.'
        }
        failure {
            echo '❌ Pipeline failed or exited early.'
        }
    }
}
