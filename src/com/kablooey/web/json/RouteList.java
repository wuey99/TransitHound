package com.kablooey.web.json;

import java.io.IOException;
import java.util.Enumeration;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class RouteList
 */
public class RouteList extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public RouteList() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		System.out.println(": RouteList: " + request.getParameterNames());
		
		Enumeration<String> parameterNames = request.getParameterNames();
		
        while (parameterNames.hasMoreElements()) {
        	String paramName = parameterNames.nextElement();
        	System.out.println(": paramName: " + paramName);
        	String[] paramValues = request.getParameterValues(paramName);
        	for (int i = 0; i < paramValues.length; i++) {
        		String paramValue = paramValues[i];
        		System.out.println(": \t: " + paramValue);      		
        	}
        }
		
		response.getWriter().append("Served at: ").append(request.getContextPath());
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
