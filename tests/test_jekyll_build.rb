# Build Test for Rakefile written in Ruby
require 'minitest/autorun'

class TestJekyllBuild < Minitest::Test
  def test_jekyll_build_exits_successfully
    result = `jekyll build`
    assert $?.success?, "Jekyll build command did not exit successfully.\nOutput:\n#{result}"
  end
end
