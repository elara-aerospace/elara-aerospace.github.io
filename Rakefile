# Rakefile
require 'rake'
require 'rake/testtask'
require 'fileutils'

desc 'Build the Jekyll site'
task :build do
  puts "Building the Jekyll site..."
  sh "jekyll build"
  puts "Jekyll build completed."
end

desc 'Clean the site'
task :clean do
  puts "Cleaning the site..."
  sh "jekyll clean"
  puts "Site cleaned."
end

desc 'Test the Jekyll site'
Rake::TestTask.new do |t|
  t.libs << "test"
  t.test_files = FileList['tests/test_jekyll_build.rb']
  t.verbose = true
end

desc 'Default task: Build and Test'
task default: [:clean, :build, :test]
