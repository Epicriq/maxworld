import sqlite3
from config import PATHS
from system.ctx import Context
from system.man import BaseManager

log = Context.init_logger(__name__)

class DBManager(BaseManager):
    def __init__(self, game):
        super().__init__()

        # Подключение к БД
        self.conn = sqlite3.connect(PATHS["file_database"])
        self.cursor = self.conn.cursor()
        self.InitTables()


    ''' Методы для простоты обращение к БД '''
    def _(self):
        self.cursor.executescript('''
        ''')
    
    ''' Создание нового игрока '''
    def NewPlayer(self, player, info, state, characteristics):
        # сначала сохраняем все его данные по таблицам:

        self.cursor.executescript(f'''
            INSERT INTO characteristics (strength, endurance, dexterity, perception, intelligence, wisdom) 
            VALUES (
                {characteristics.strength},
                {characteristics.endurance},
                {characteristics.dexterity},
                {characteristics.perception},
                {characteristics.intelligence},
                {characteristics.wisdom}
            );
        ''')
        
        self.cursor.executescript(f'''
            INSERT INTO state (hits, mana, energy, morale) 
            VALUES (
                {state.hits},
                {state.mana},
                {state.energy},
                {state.morale}
            );
        ''')

        self.cursor.executescript(f'''
            INSERT INTO info (lvl, exp, age, gender, height, weight, location_id) 
            VALUES (
                {info.lvl},
                {info.exp},
                {info.age},
                {info.gender},
                {info.height},
                {info.weight},
                {info.location_id}                
            );
        ''')
        
        # наконец прописываем его в player
        self.cursor.executescript(f'''
            INSERT INTO player (name, info_id, state_id, characteristics_id, abilities_id, skills_id, spells_id) 
            VALUES (
                {player.name}, 
                {player.info_id}, 
                {player.state_id}, 
                {player.characteristics_id}, 
                {player.abilities_id}, 
                {player.skills_id}, 
                {player.spells_id}
            );
        ''')

    ''' Тут происходит инициализация структуры БД '''
    # Создание таблиц (если их нет)
    def InitTables(self):
        # Таблица info
        self.cursor.executescript('''                         
            CREATE TABLE IF NOT EXISTS info (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                lvl INTEGER,
                exp INTEGER, 
                age INTEGER,
                gender TEXT,
                height INTEGER,
                weight INTEGER,
                location_id INTEGER,
                FOREIGN KEY (location_id) REFERENCES location(id)
            );
        ''')
        
        # Таблица state
        self.cursor.executescript('''                         
            CREATE TABLE IF NOT EXISTS state (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                hits INTEGER,
                mana INTEGER,
                energy INTEGER,
                morale INTEGER
            );
        ''')
        
        # Таблица Characteristics
        self.cursor.executescript('''
            CREATE TABLE IF NOT EXISTS сharacteristics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                strength INTEGER,
                endurance INTEGER,
                dexterity INTEGER,
                perception INTEGER,
                intelligence INTEGER,
                wisdom INTEGER
            );
        ''')
        
        # Таблица для Abilities, Skill, Spell
        self.cursor.executescript('''                         
            CREATE TABLE IF NOT EXISTS ass (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                mode TEXT,
                name TEXT,
                type TEXT,
                triggering_chance REAL,
                cooldown: REAL,
                current_cooldown: REAL,
                                
                attack_bonus: REAL,
                defense_bonus: REAL,
                hit_recovery_bonus: REAL,
                mana_recovery_bonus: REAL,
                energy_recovery_bonus: REAL,
                moral_recovery_bonus: REAL,

                physical_damage: REAL,
                magic_damage: REAL,
                hits_damage: REAL,
                mana_damage: REAL,
                energy_damage: REAL,
                moral_damage: REAL,

                hits_cost: REAL,
                mana_cost: REAL,
                energy_cost: REAL,
                morale_cost: REAL
            );
        ''')
        
        
        # Таблица Inventory
        self.cursor.executescript('''                         
            CREATE TABLE IF NOT EXISTS inventory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                owner_id INTEGER,
                name TEXT,
                count INTEGER,
                FOREIGN KEY (owner_id) REFERENCES player(id)
            );                
        ''')
        
        
        # Таблица player (игроки)
        self.cursor.executescript('''
            CREATE TABLE IF NOT EXISTS player (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                info_id INTEGER, 
                state_id INTEGER, 
                characteristics_id INTEGER, 
                abilities_id INTEGER, 
                skills_id INTEGER, 
                spells_id INTEGER, 
                FOREIGN KEY (info_id) REFERENCES info(id),
                FOREIGN KEY (state_id) REFERENCES state(id),
                FOREIGN KEY (characteristics_id) REFERENCES characteristics(id),
                FOREIGN KEY (abilities_id) REFERENCES ass(id),
                FOREIGN KEY (skills_id) REFERENCES ass(id),
                FOREIGN KEY (spells_id) REFERENCES ass(id)
            );
        ''')
        
        # Таблица npc (NPC)
        self.cursor.executescript('''
            CREATE TABLE IF NOT EXISTS npc (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                health INTEGER DEFAULT 50,
                attack INTEGER DEFAULT 5,
                dialog_id INTEGER, -- ссылка на диалог
                location_id INTEGER,
                FOREIGN KEY (location_id) REFERENCES locations(id),
                FOREIGN KEY (dialog_id) REFERENCES dialogs(id)                         
            );
        ''')
        
        # Таблица item (предметы)
        self.cursor.executescript('''
            CREATE TABLE IF NOT EXISTS item (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                type TEXT CHECK(type IN ('weapon', 'armor', 'potion', 'quest', 'misc')),
                attack_bonus INTEGER DEFAULT 0,
                defense_bonus INTEGER DEFAULT 0,
                health_restore INTEGER DEFAULT 0,
                value INTEGER DEFAULT 1,
                description TEXT
            );                         
        ''')
        
        # Таблица location (локации)
        self.cursor.executescript('''
            CREATE TABLE IF NOT EXISTS location (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                north_location_id INTEGER,
                east_location_id INTEGER,
                south_location_id INTEGER,
                west_location_id INTEGER,
                FOREIGN KEY (north_location_id) REFERENCES location(id),
                FOREIGN KEY (east_location_id) REFERENCES location(id),
                FOREIGN KEY (south_location_id) REFERENCES location(id),
                FOREIGN KEY (west_location_id) REFERENCES location(id)
            );                         
        ''')
        
        # Таблица quest (квесты)
        self.cursor.executescript('''
            CREATE TABLE IF NOT EXISTS quest (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                reward_exp INTEGER DEFAULT 0,
                reward_item_id INTEGER,
                is_completed BOOLEAN DEFAULT FALSE,
                required_item_id INTEGER,
                required_kill_npc_id INTEGER,
                FOREIGN KEY (reward_item_id) REFERENCES item(id),
                FOREIGN KEY (required_item_id) REFERENCES item(id),
                FOREIGN KEY (required_kill_npc_id) REFERENCES npc(id)
            );
        ''')
        
        # Таблица dialog (диалоги)
        self.cursor.executescript('''
            CREATE TABLE IF NOT EXISTS dialog (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                npc_id INTEGER,
                text TEXT NOT NULL,
                next_dialog_id INTEGER,
                gives_quest_id INTEGER,
                FOREIGN KEY (npc_id) REFERENCES npc(id),
                FOREIGN KEY (next_dialog_id) REFERENCES dialog(id),
                FOREIGN KEY (gives_quest_id) REFERENCES quest(id)
            );                         
        ''')
        
        # Таблица inventory (инвентарь игрока)
        self.cursor.executescript('''
            CREATE TABLE IF NOT EXISTS inventory (
                player_id INTEGER,
                item_id INTEGER,
                quantity INTEGER DEFAULT 1,
            FOREIGN KEY (player_id) REFERENCES player(id),
            FOREIGN KEY (item_id) REFERENCES item(id),
            PRIMARY KEY (player_id, item_id));                         
        ''')
        #cursor.executescript('''                         
        #''')
        