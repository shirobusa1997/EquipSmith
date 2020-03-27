from django.db import models
from django.contrib.auth import get_user_model

from enum import Enum

# Create your models here.
class Equipments(models.Model):
	class EQUIP_ATTRIBUTE(Enum):
		book = ('book', '書籍')
		desktopcomputer = ('depc', 'デスクトップPC')
		laptopcomputer = ('lapc', 'ノートPC')
		workstation = ('wkst', 'ワークステーション')
		display = ('dspl', 'PCディスプレイ')
		pcsupply = ('pcsp', 'PC周辺機器')
		vrdevice = ('vrdv', 'VRデバイス')
		ardevice = ('ardv', 'ARデバイス')
		projector = ('prjc', 'プロジェクター')
		screen = ('scrn', 'スクリーン')
		smartphone = ('smph', 'スマートフォン')
		tabletdevice = ('tbdv', 'タブレット端末')
		toolkit = ('tool', '工具類')

		@classmethod
		def getValue(cls, member):
			return cls[member].value[0]

	class EQUIP_STATUS(Enum):
		available = ('avlb', '利用可能')
		lending = ('lend', '貸出中')
		assigning = ('asgn', '割当中')
		lost = ('lost', '紛失')

		@classmethod
		def getValue(cls, member):
			return cls[member].value[0]

	id = models.CharField('備品ID', max_length = 16, primary_key = True)
	name = models.CharField('備品名', blank=False, max_length = 255)
	equip_attribute = models.CharField('種類', null=True, max_length = 4, choices = [x.value for x in EQUIP_ATTRIBUTE])
	equip_status = models.CharField('ステータス', null=True, max_length = 4, choices = [x.value for x in EQUIP_STATUS])
	registered_date = models.DateTimeField('登録年月日', auto_now = True)
	remarks = models.CharField('備考', max_length=255, blank=True)


class Records(models.Model):
	id = models.AutoField('処理ID', primary_key = True, editable=False)
	equipid = models.ForeignKey(Equipments, on_delete = models.CASCADE)
	userid = models.ForeignKey(get_user_model(), on_delete = models.CASCADE, default = 1)
	recorded_date = models.DateTimeField('申請日時', auto_now = True)