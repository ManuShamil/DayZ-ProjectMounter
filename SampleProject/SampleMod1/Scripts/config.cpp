class CfgPatches
{
	class SampleMod1
	{
		units[] = {};
		weapons[] = {};
		requiredVersion = 0.1;
		requiredAddons[] = {};
	};
};
class CfgMods
{
	class SampleMod1
	{
		dir = "SampleMod1\Scripts";
		extra = 0;
		type = "mod";
		dependencies[] = {"Mission"};
		class defs
		{
			class missionScriptModule
			{
				value = "";
				files[] = {"SampleMod1\Scripts\5_Mission"};
			};
		};
	};
};
