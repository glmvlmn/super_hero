from utils.load.list import Get_value


class Value:


    def search_hight(api_data):
        list_hero_dict = []
        hero_hight = 0
        for hero in api_data:

            occupation = Get_value.with_key(hero['work'], "occupation")
            gender = Get_value.with_key(hero["appearance"], "gender")
            if occupation != '-' and gender != '-':
                hieght = Get_value.with_key(hero["appearance"], "height")
                rost = hieght[1].split()
                if float(rost[0]) > hero_hight:
                    hero_hight = float(rost[0])
                    name = Get_value.with_key(hero, 'name')
        list_hero_dict.append(name)

        print(*list_hero_dict)
        return ''.join(list_hero_dict)







#value=Value()