pipeline {
    agent any

    stages {
        stage('Prepare Virtual Environment') {
            steps {
                script {
                    sh '''
                        echo "🛠 Checking Python version..."
                        python3 --version

                        echo "📦 Creating virtual environment if it doesn't exist..."
                        if [ ! -d "venv" ]; then
                            python3 -m venv venv
                        fi

                        echo "⬆️ Upgrading pip..."
                        venv/bin/pip install --upgrade pip
                    '''
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    sh '''
                        echo "📥 Installing project dependencies..."
                        venv/bin/pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Kafka Producer') {
            steps {
                script {
                    sh '''
                        echo "🚀 Running Kafka producer..."
                        venv/bin/python producer.py
                    '''
                }
            }
        }

        stage('Run Spark Consumer') {
            steps {
                script {
                    sh '''
                        echo "🔄 Running Spark consumer..."
                        spark-submit --master local[*] consumer.py
                    '''
                }
            }
        }

        stage('Clean Up') {
            steps {
                echo '🧹 Pipeline execution complete. Clean up if needed.'
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
