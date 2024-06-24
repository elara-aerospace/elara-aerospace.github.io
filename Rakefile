# Rakefile
require 'rake/testtask'

# Define the test task
Rake::TestTask.new do |t|
  t.libs << "test"
  t.test_files = FileList['tests/test_*.rb']
  t.verbose = true
end

desc 'Default task: Run tests'
task default: :test
