/**
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */
package org.apache.pinot.core.query.request.context.utils;

import org.apache.pinot.core.query.aggregation.function.AggregationFunction;
import org.apache.pinot.core.query.aggregation.function.DistinctAggregationFunction;
import org.apache.pinot.core.query.request.context.QueryContext;


@SuppressWarnings("rawtypes")
public class QueryContextUtils {
  private QueryContextUtils() {
  }

  /**
   * Returns {@code true} if the given query is a selection query, {@code false} otherwise.
   */
  public static boolean isSelectionQuery(QueryContext query) {
    return query.getAggregationFunctions() == null;
  }

  /**
   * Returns {@code true} if the given query is an aggregation query, {@code false} otherwise.
   */
  public static boolean isAggregationQuery(QueryContext query) {
    AggregationFunction[] aggregationFunctions = query.getAggregationFunctions();
    return aggregationFunctions != null && (aggregationFunctions.length != 1
        || !(aggregationFunctions[0] instanceof DistinctAggregationFunction));
  }

  /**
   * Returns {@code true} if the given query is a distinct query, {@code false} otherwise.
   */
  public static boolean isDistinctQuery(QueryContext query) {
    AggregationFunction[] aggregationFunctions = query.getAggregationFunctions();
    return aggregationFunctions != null && aggregationFunctions.length == 1
        && aggregationFunctions[0] instanceof DistinctAggregationFunction;
  }
}
