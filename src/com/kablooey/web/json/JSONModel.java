package com.kablooey.web.json;

import java.io.PrintWriter;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

public class JSONModel {
	
	protected void serialize (PrintWriter writer, boolean printPretty) {
		getGson (printPretty).toJson (this, writer);
	}
	
	protected static Gson getGson(boolean printPretty) {
		if (printPretty) {
			return new GsonBuilder().setPrettyPrinting().create();
		}
		
		return new Gson();
	}
}
