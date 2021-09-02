from ..models import *

adminUser = UserBuilder()

adminUser.role("admin") \
  .name("Alarm System Team") \
  .email("alarmsystem.su.fmi@gmail.com")