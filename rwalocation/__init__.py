from .main import Province

app = Province()

def district(district_name=None):
  if district_name:
    return app.district(district_name)
  return app.district()

def province(province_name=None):
  if province_name:
    return app.province(province_name)
  return app.province()

def location(location_name=None):
  if location_name:
    return app.location(location_name)
  return app.location()
