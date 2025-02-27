import pygame
from data import GameData, GameController

class Inventory(object):
    def __init__(self, GameController: GameController, GameData: GameData):
        self.GameController = GameController
        self.GameData = GameData

        self.current_items = []
        self.current_key_items = []
        self.bag_slots = ["inventory_menu", "key_inventory_menu"]
        self.current_bag_slot = 0
        self.selected_item = None

    def select_item(self, selected_item):
        self.selected_item = selected_item

    def bag_left(self):
        self.bag_slots.append(self.bag_slots.pop(self.bag_slots.index(self.bag_slots[0])))

    def change_bag_slot(self):
        self.GameController.MenuManager.self.bag_slots[0] = True

    def bag_slot_right(self):
        self.GameController.MenuManager.deactivate_menu(self.bag_slots[self.current_bag_slot])
        if self.current_bag_slot < (len(self.bag_slots)-1):
            self.current_bag_slot +=1
        elif self.current_bag_slot == (len(self.bag_slots)-1):
            self.current_bag_slot = 0
        self.GameController.MenuManager.activate_menu(self.bag_slots[self.current_bag_slot])
        self.GameController.current_menu = self.bag_slots[self.current_bag_slot]
        self.GameController.set_keyboard_manager(self.GameData.menu_list[self.GameController.current_menu].associated_manager)



    def bag_slot_left(self):
        self.GameController.MenuManager.deactivate_menu(self.bag_slots[self.current_bag_slot])
        if self.current_bag_slot > 0:
            self.current_bag_slot -=1
        else:
            self.current_bag_slot = (len(self.bag_slots)-1)
        self.GameController.MenuManager.activate_menu(self.bag_slots[self.current_bag_slot])
        self.GameController.current_menu = self.bag_slots[self.current_bag_slot]
        self.GameController.set_keyboard_manager(self.GameData.menu_list[self.GameController.current_menu].associated_manager)


    def reset_bag_slot(self):
        self.current_bag_slot = 0

    def get_item(self, item_name: str, quantity_acquired: int):
        if item_name in self.current_items:
            self.GameData.item_list[item_name].quantity += quantity_acquired
        else:
            self.current_items.append(self.GameData.item_list[item_name].name)
            self.GameData.item_list[item_name].quantity += quantity_acquired

    def use_up_item(self, item_name: str, quantity_used: int):
        #TODO: Make sure this can't go below 0
        if self.GameData.item_list[item_name].quantity > quantity_used:
            self.GameData.item_list[item_name].quantity -= quantity_used
        elif self.GameData.item_list[item_name].quantity == quantity_used:
            self.current_items.pop(self.GameData.item_list[item_name].name)
            self.GameData.item_list[item_name].quantity -= quantity_used
        else:
            print("you cannot use that now")

    def get_key_item(self, key_item_name: str):
        self.current_key_items.append(self.GameData.key_item_list[key_item_name].name)
        self.GameData.key_item_list[key_item_name].quantity = 1

    def use_up_key_item(self, key_item_name: str):
        self.GameData.key_item_list[key_item_name].quantity = 0
        self.current_key_items.pop(self.GameData.key_item_list[key_item_name].name)



class Item(object):
    def __init__(self, name, GameData, GameController):
        self.GameController = GameController
        self.GameData = GameData
        self.name = name
        self.quantity = 0
        pass

    def use_item(self):
        print("You used the " + self.name)

class KeyItem(object):
    def __init__(self, name, GameData, GameController):
        self.GameController = GameController
        self.GameData = GameData
        self.name = name
        self.quantity = 0
        pass

    def use_item(self):
        print("You used the " + self.name)