# Build Test for Rakefile written in Ruby
require 'minitest/autorun'
require 'fileutils'

class TestJekyllBuild < Minitest::Test
  def setup
    @site_dir = "_site"
    @index_file = File.join(@site_dir, "index.html")
  end

  def test_site_directory_exists
    assert Dir.exist?(@site_dir), "The _site directory should exist after Jekyll build."
  end

  def test_index_file_exists
    assert File.exist?(@index_file), "The index.html file should exist in the _site directory."
  end

  def teardown
    FileUtils.rm_rf(@site_dir) if Dir.exist?(@site_dir)
  end
end
