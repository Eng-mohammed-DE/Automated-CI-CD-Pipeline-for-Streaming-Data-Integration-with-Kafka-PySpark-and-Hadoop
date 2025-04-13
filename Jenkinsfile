stage('Debug VENV Path') {
    steps {
        script {
            sh '''
                echo "🔍 Checking if /home/eng-mohammed/master_node/venv exists"
                if [ -d "/home/eng-mohammed/master_node/venv" ]; then
                    echo "✅ venv directory found"
                else
                    echo "❌ venv directory not found"
                fi

                echo "🔍 Listing contents of /home/eng-mohammed/master_node"
                ls -l /home/eng-mohammed/master_node

                echo "🔍 Listing contents of /home/eng-mohammed/master_node/venv/bin"
                ls -l /home/eng-mohammed/master_node/venv/bin || echo "❌ Could not list venv/bin"
                
                echo "🔍 Checking if 'activate' script exists"
                if [ -f "/home/eng-mohammed/master_node/venv/bin/activate" ]; then
                    echo "✅ activate script found"
                else
                    echo "❌ activate script NOT found"
                fi
            '''
        }
    }
}
