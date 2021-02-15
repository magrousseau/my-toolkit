from mytoolkit.get_data import clean_text

def test_clean_tex_len():
  assert len(clean_text('hello world , !!')) != 0
