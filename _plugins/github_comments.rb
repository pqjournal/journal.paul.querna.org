class Jekyll::Post
  alias :to_liquid_original :to_liquid

  def _get_comments(comments_slug)
    site.source
    comments = []
    Dir["#{site.source}/_comments/#{comments_slug}/*"].sort.each do |comment|
      next unless File.file?(comment) and File.readable?(comment)
      data = YAML::load_file(comment)
      comments << data
    end
    comments
  end

  def to_liquid
    hash = to_liquid_original
    comments_slug = self.date.strftime("%Y-%m-%d") + "-" + self.slug
    hash['comments'] = _get_comments(comments_slug)
    hash['comments_slug'] = comments_slug
    hash['comments_lenght'] = hash['comments'].length
    hash
  end
end