import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import subprocess
import shutil
import struct

class MusicModApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mario Odyssey Music Mod Builder")

        self.file_path = tk.StringVar()
        self.selected_song = tk.StringVar()
        self.loop_start = tk.StringVar()
        self.loop_end = tk.StringVar()
        self.song_list = []
        self.song_map = {}  # Display Name -> Internal File ID

        self.load_embedded_song_list()
        self.build_ui()

    def load_embedded_song_list(self):
        embedded_list = """
Beforegk Nk48 Dspadpem,RsBgmBeforeGK.nk48.dspadpem
Bossdragon S 48 Dspadpem,RsBgmBossDragon.s.48.dspadpem
Bossgatekeeper,RsBgmBossGateKeeper
Bosshaikai A Nk48,RsBgmBossHaikai_A.nk48
Bossmagma,RsBgmBossMagma
Bossmofumotu Nk48 Dspadpem,RsBgmBossMofumotu.nk48.dspadpem
Citycafe01 Nk48,RsBgmCityCafe01.nk48
Citycafe01Radio Nk22,RsBgmCityCafe01Radio.nk22
Cityscenario01,RsBgmCityScenario01
Cityscenario01Strain Nk48,RsBgmCityScenario01Strain.nk48
Cityscenario03,RsBgmCityScenario03
Cityscenario03Clct Nk48,RsBgmCityScenario03Clct.nk48
Cityscenario03Jp Nk48 Dspadpem,RsBgmCityScenario03Jp.nk48.dspadpem
Cityscenario04 Dspadpem,RsBgmCityScenario04.dspadpem
Citysessionalll,RsBgmCitySessionAlll
Clashfirstk48 Dspadpem,RsBgmClashFirstk48.dspadpem
Demokoopaappear Ingame0598 Nk48,RsBgmDemoKoopaAppear_Ingame0598.nk48...
Demokoopalv2Start Dspadpem,RsBgmDemoKoopalv2Start.dspadpem
Demomeetcapfirsta,RsBgmDemoMeetCapFirstA
Deserttown Nk22 Dspadpem,RsBgmDesertTown.nk22.dspadpem
Deserttownclctnk 48 Dspadpem,RsBgmDesertTownClctnk.48.dspadpem
Dinosaur,RsBgmDinosaur
E3Title2 Nk48,RsBgmE3Title2.nk48
E3Titlenk48 Dspadpem,RsBgmE3Titlenk48.dspadpem
Endrock8Bit Nk48 Dspadpem,RsBgmEndRock8bit.nk48.dspadpem
Endrockjpradio Nk22,RsBgmEndRockJpRadio.nk22
Endrockip Nk48 Dspadpem,RsBgmEndRockip.nk48.dspadpem
Endrocknk 48 Dspadpem,RsBgmEndRocknk.48.dspadpem
Exathletick48 Dspadpem,RsBgmExAthletick48.dspadpem
Exbonus,RsBgmExBonus
Exchika2,RsBgmExChika2
Excold Dspadpem,RsBgmExCold.dspadpem
Expsyche Dspadpem,RsBgmExPsyche.dspadpem
Hat,RsBgmHat
Jgbosshaikaiappear Nk,RsBgmJgBossHaikaiAppear.nk
Kinopiobrigadenk32 Dspadpem,RsBgmKinopioBrigadenk32.dspadpem
Laketunnel Dspadpem,RsBgmLakeTunnel.dspadpem
Lavatown,RsBgmLavaTown
M1Plk32 Dspadpem,RsBgmM1PLk32.dspadpem
M1Ug,RsBgmM1UG.
Minigame01Fs 48 Dspadpcem,RsBgmMiniGame01fs.48.dspadpcem
Moonchurch Dspadpem,RsBgmMoonChurch.dspadpem
Moondungeon Nk48,RsBgmMoonDungeon.nk48
Peachcastle,RsBgmPeachCastle
Race,RsBgmRace
Racehurry,RsBgmRaceHurry
Raceresult Dspadpem,RsBgmRaceResult.dspadpem
Radiocontrolcar,RsBgmRadioControlCar
Raidworld Fs,RsBgmRaidWorld.fs
Seskygkzone Sg 48 Dspadpem,RsBgmSeSkyGkZone.sg.48.dspadpem
Sea01Ballslope Nk48 Dspadpcem,RsBgmSea01BallSlope.nk48.dspadpcem
Sea01Beach Nk22 Dspadpcem,RsBgmSea01beach.nk22.dspadpcem
Shop01 K48 Dspadpem,RsBgmShop01.k48.dspadpem
Shop01Radio K48 Dspadpem,RsBgmShop01Radio.k48.dspadpem
Shop01Radio Tmp K48 Dspadpem,RsBgmShop01Radio_tmp.k48.dspadpem
Shop02 K48 Dspadpem,RsBgmShop02.k48.dspadpem
Shop02Radio K48 Dspadpem,RsBgmShop02Radio.k48.dspadpem
Shop03 K48 Dspadpem,RsBgmShop03.k48.dspadpem
Shop03Radio K48 Dspadpem,RsBgmShop03Radio.k48.dspadpem
Shop04 K48 Dspadpem,RsBgmShop04.k48.dspadpem
Shop04Radio K48 Dspadpem,RsBgmShop04Radio.k48.dspadpem
Shopclctk48 Dspadpem,RsBgmShopClctk48.dspadpem
Sky02 K48,RsBgmSky02.k48
Slotroom Nk48,RsBgmSlotRoom.nk48
Snow,RsBgmSnow
Snowenv002 Fs,RsBgmSnowEnv002.fs
Snowenv003 Fs,RsBgmSnowEnv003.fs
Snowenv004,RsBgmSnowEnv004
Snowenv005 Fs,RsBgmSnowEnv005.fs
Snowenv006 Fs,RsBgmSnowEnv006.fs
Snowenv007 Fs,RsBgmSnowEnv007.fs
Snowenv008 Fs,RsBgmSnowEnv008.fs
Snowenv009 Fs,RsBgmSnowEnv009.fs
Snowenv010 Fs,RsBgmSnowEnv010.fs
Snowtown,RsBgmSnowTown
Snowtownjingle Fs 32 Dspadpem,RsBgmSnowTownJingle.fs.32.dspadpem
Snowtownraceentrance S 48 Dspadpem,RsBgmSnowTownRaceEntrance.s.48.dspadpem
Staffroll,RsBgmStaffRoll
Titlenk48 Dspadpem,RsBgmTitlenk48.dspadpem
Igtitle Nk48,RsBgmigTitle.nk48
Desertworld 001,StmDesertWorld_001
Desertworld 002,StmDesertWorld_002
Desertworld 003,StmDesertWorld_003
Desertworld 004,StmDesertWorld_004
Desertworld 005,StmDesertWorld_005
Desertworld 006,StmDesertWorld_006
Desertworld 007,StmDesertWorld_007
Desertworld 008,StmDesertWorld_008.
Desertworld 009,StmDesertWorld_009
Desertworld 01,StmDesertWorld_01
Desertworld 010,StmDesertWorld_010
Desertworld 011,StmDesertWorld_011
Desertworld 013,StmDesertWorld_013
Desertworld 014,StmDesertWorld_014
Bossbreeda,StmRsBgmBossBreeda
Bossdra,StmRsBgmBossDra
Bossforest,StmRsBgmBossForest
Bossgolem,StmRsBgmBossGolem
Bosshaikai B,StmRsBgmBossHaikai_B
Bosskoo,StmRsBgmBossKoo
Bosskoopa02,StmRsBgmBossKoopa02
Cityscen,StmRsBgmCityScen
Cityscenario02,StmRsBgmCityScenario02
Cityscenario03,StmRsBgmCityScenario03
Citysession,StmRsBgmCitySession
Clashsecond,StmRsBgmClashSecond
Demoworldmap,StmRsBgmDemoWorldMap
Desertm,StmRsBgmDesertM
Desertmainparade,StmRsBgmDesertMainParade
Desertnight,StmRsBgmDesertNight
Exathletico2,StmRsBgmExAthleticO2
Exchika,StmRsBgmExChika
Exhat,StmRsBgmExHat
Exruin,StmRsBgmExRuin
Fall,StmRsBgmFall
Forest,StmRsBgmForest
Jaguar,StmRsBgmJaguar
Lakescenario1,StmRsBgmLakeScenario1
Lakescenario2,StmRsBgmLakeScenario2
Lava,StmRsBgmLava
Moon,StmRsBgmMoon
Moonescape,StmRsBgmMoonEscape
Moonparade,StmRsBgmMoonParade
Sea01,StmRsBgmSea01
Sea02,StmRsBgmSea02
Sky01,StmRsBgmSky01
        """.strip()

        for line in embedded_list.splitlines():
            if line.strip() and "," in line:
                display_name, internal_id = map(str.strip, line.split(",", 1))
                self.song_map[display_name] = internal_id

        self.song_list = list(self.song_map.keys())

    def build_ui(self):
        tk.Label(self.root, text="🎵 Select Custom Music File:").pack(anchor='w', padx=10, pady=(10, 0))
        tk.Entry(self.root, textvariable=self.file_path, width=50).pack(padx=10)
        tk.Button(self.root, text="Browse", command=self.browse_file).pack(pady=(0, 10))

        tk.Label(self.root, text="🎮 Replace In-Game Song:").pack(anchor='w', padx=10)
        self.song_dropdown = ttk.Combobox(self.root, values=self.song_list, textvariable=self.selected_song)
        self.song_dropdown.pack(padx=10, pady=(0, 10))

        tk.Label(self.root, text="🔁 Loop Start (hh:mm:ss):").pack(anchor='w', padx=10)
        tk.Entry(self.root, textvariable=self.loop_start).pack(padx=10)

        tk.Label(self.root, text="🔁 Loop End (hh:mm:ss):").pack(anchor='w', padx=10)
        tk.Entry(self.root, textvariable=self.loop_end).pack(padx=10)

        tk.Button(self.root, text="Convert & Build Mod Folder", command=self.build_mod).pack(pady=10)

    def browse_file(self):
        path = filedialog.askopenfilename(filetypes=[("Audio files", "*.mp3 *.wav")])
        if path:
            self.file_path.set(path)

    def generate_prefetch(self, bfstm_path, output_path):
        try:
            with open(bfstm_path, "rb") as f:
                data = f.read()

            if data[0:4] != b"FSTM":
                raise ValueError("Invalid BFSTM file")

            # Extract track length from bytes 0x40-0x43
            total_samples = struct.unpack_from("<I", data, 0x40)[0]
            prefetch_bytes = struct.pack("<I", total_samples)

            with open(output_path, "wb") as f:
                f.write(prefetch_bytes)
        except Exception as e:
            raise RuntimeError(f"Prefetch generation failed: {e}")

    def build_mod(self):
        if not self.file_path.get() or not self.selected_song.get():
            messagebox.showwarning("Missing Info", "Please select a file and a target song.")
            return

        internal_id = self.song_map.get(self.selected_song.get())
        if not internal_id:
            messagebox.showerror("Error", "Selected song does not have an internal ID.")
            return

        output_folder = os.path.join(os.path.dirname(__file__), "mod_output", internal_id)
        os.makedirs(output_folder, exist_ok=True)

        wav_path = os.path.join(output_folder, "converted.wav")
        bfstm_path = os.path.join(output_folder, f"{internal_id}.bfstm")

        try:
            # Convert to WAV with ffmpeg
            subprocess.run(["ffmpeg", "-i", self.file_path.get(), wav_path], check=True)

            # Convert to .bfstm (assumes LoopingAudioConverter or similar is available)
            converter_path = os.path.join(os.path.dirname(__file__), "LoopingAudioConverter.exe")
            if not os.path.exists(converter_path):
                raise FileNotFoundError("LoopingAudioConverter.exe not found. Please make sure it's in the same folder as this script.")
            subprocess.run([converter_path, wav_path, "-o", bfstm_path], check=True)

            # Generate prefetch internally
            prefetch_path = os.path.join(output_folder, f"{internal_id}.prefetchinfo")
            self.generate_prefetch(bfstm_path, prefetch_path)

            # Build LayeredFS folder structure
            mod_path = os.path.join(output_folder, "atmosphere/contents/.../romfs/Sound/Stream")
            os.makedirs(mod_path, exist_ok=True)
            shutil.copy(bfstm_path, os.path.join(mod_path, f"{internal_id}.bfstm"))

            messagebox.showinfo("Success", f"Mod folder created at:\n{output_folder}")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"An error occurred during processing:\n{e}")
        except Exception as e:
            messagebox.showerror("Error", f"Unexpected error:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicModApp(root)
    root.mainloop()
