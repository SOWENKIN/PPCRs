patch_label_list = ['肿瘤区域', '淋巴区域', '脂肪区域', '上皮区域', '钙化区域', '坏死区域', '其他区域']
patch_label_dict = {'Tumor': 0, 'tumor': 0, 'tumore': 0, '肿瘤': 0, '肿瘤区域': 0,
              'lym': 1, 'lyn': 1, '淋巴': 1, '淋巴聚集': 1, '淋巴管': 1, '小叶':1, '淋巴区域': 1,
              'fat': 2, 'fas': 2, '脂肪': 2, '脂肪区域': 2,
              'epi': 3, '导管上皮': 3, '导管上皮b': 3, '上皮区域': 3, '腺上皮': 3,
              'cal': 4, '钙化': 4, '钙化区域': 4,
              'nec': 5, '坏死': 5, '坏死区域': 5,
              'vas': 6, 'val': 6, '血管': 6, '血管区域': 6,
              'oth': 6, '其他': 6, '其他区域': 6,
              '神经': 6,
              }


point_label_list = ['肿瘤细胞', '纤维(母)细胞', '淋巴细胞', '巨噬细胞', '浆细胞', '嗜酸性粒细胞', '中性粒细胞', '上皮细胞']
point_label_dict = {
    'T': 0, 'Tumor': 0, 'tumor': 0, 'tumore': 0, '肿瘤': 0, '肿瘤细胞': 0,
    'F': 1, '纤维细胞': 1, '纤维母细胞': 1, '纤维细胞/纤维母细胞': 1, '纤维(母)细胞': 1,
    'L': 2, '淋巴细胞': 2,
    'M': 3, '巨噬细胞': 3,
    'P': 4, '浆细胞': 4,
    'E': 5, '嗜酸性粒细胞': 5,
    'N': 6, '中性粒细胞': 6,
    'vas': 7, 'val': 7, '血管': 6, '血管区域': 7, '血管内皮': 7, '正常上皮': 7,
    }


label_list = ['肿瘤区域', '淋巴区域', '脂肪区域', '上皮区域', '钙化区域', '坏死区域', '其他区域']
label_dict = {'Tumor': 0, 'tumor': 0, 'tumore': 0, '癌': 0, '肿瘤': 0, '肿瘤区域': 0,
              'lym': 1, 'lyn': 1, '淋巴': 1, '淋巴聚集': 1, '淋巴管': 1, '小叶':1, '淋巴区域': 1,
              'fat': 2, 'fas': 2, '脂肪': 2, '脂肪区域': 2,
              'epi': 3, '导管上皮': 3, '导管上皮b': 3, '上皮区域': 3, '腺上皮': 3,
              'cal': 4, '钙化': 4, '钙化区域': 4,
              'nec': 5, '坏死': 5, '坏死区域': 5,
              'vas': 6, 'val': 6, '血管': 6, '血管区域': 6,
              'oth': 6, '其他': 6, '其他区域': 6,
              '神经': 6,
              }

label_color_dict = {'肿瘤区域': (250, 25, 14), '坏死区域': (127, 127, 127),
                                '脂肪区域': (222, 234, 30), '钙化区域': (7, 231, 237),
                                '淋巴区域': (0, 176, 80), '上皮区域': (0, 112, 192), '其他区域': (0, 112, 192)}
